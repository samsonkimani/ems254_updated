from flask import Blueprint

from flask import jsonify, request
from flask_jwt_extended import jwt_required

from utils.user_account import AccountService
from utils.TransactionServices import TransactionServices
from auth.auth import Authentication

transaction_bp = Blueprint('transaction_bp', __name__)

account_service = AccountService()
transaction_service = TransactionServices()
user_authenticator = Authentication()

@jwt_required
@transaction_bp.route('/transact', methods=['POST'])
def create_transaction():
    sender_id = user_authenticator.get_authenticated_user()
    account_number = request.json.get('account_number')
    receiver_id = account_service.get_user_id_from_account_number(account_number)
    amount = request.json.get('amount')
    if not account_number:
        return jsonify({'message': 'account_number is required'}), 400
    if not amount:
        return jsonify({'message': 'amount is required'}), 400
    if not receiver_id:
        return jsonify({'message': 'there was an error with the account number'}), 400
    if not sender_id:
        return jsonify({'message': 'sender_id is required'}), 400
    if sender_id == receiver_id:
        return jsonify({'message': 'you cannot send money to yourself'}), 400
    account_service.transact(amount, sender_id, receiver_id)
    transaction_service.create_a_transaction(sender_id=sender_id, receiver_id=receiver_id, amount=amount)
    return jsonify({'message': 'transaction created successfully'}), 201


@jwt_required
@transaction_bp.route('/user_transactions', methods=['GET'])
def get_all_transactions():
    user_id = user_authenticator.get_authenticated_user()
    transactions = transaction_service.get_all_transactions(user_id)
    return transactions

@jwt_required
@transaction_bp.route('/transaction/<string:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    transaction = transaction_service.get_transaction(transaction_id)
    if not transaction:
        return jsonify({'message': 'transaction not found'}), 404
    return jsonify({'message': 'transaction found', 'transaction': transaction}), 200

# @jwt_required
# @transaction_bp.route('/approve/<string:transaction_id>', methods=['PATCH'])
# def approve_transaction(transaction_id):
#     transaction = transaction_service.get_transaction(transaction_id)
#     if not transaction:
#         return jsonify({'message': 'transaction not found'}), 404

#     if transaction.status == 'pending':
#         # getting user details from the transaction id
#         sender_id = transaction.sender_id
#         receiver_id = transaction.receiver_id
#         amount = transaction.amount
#         account_service.send_money(amount, sender_id, receiver_id)
#         transaction_service.approve_transaction(transaction_id)
#         return jsonify({'message': 'transaction approved'}), 200

#     return jsonify({'message': 'transaction already approved'}), 400

@jwt_required
@transaction_bp.route('/approve/<string:transaction_id>', methods=['PATCH'])
def approve_transaction(transaction_id):
    transaction = transaction_service.get_transaction(transaction_id)
    if not transaction:
        return jsonify({'message': 'transaction not found'}), 404

    if transaction.status == 'pending':
        # getting user details from the transaction id
        sender_id = transaction.sender_id
        receiver_id = transaction.receiver_id
        amount = transaction.amount
        # account_service.send_money(amount, sender_id, receiver_id)
        transaction_service.approve_transaction(transaction_id)
        return jsonify({'message': 'transaction approved'}), 200

    return jsonify({'message': 'transaction already approved'}), 400

@jwt_required
@transaction_bp.route('/cancel/<string:transaction_id>', methods=['PATCH'])
def cancel_transaction(transaction_id):
    transaction = transaction_service.get_transaction(transaction_id)
    if not transaction:
        return jsonify({'message': 'transaction not found'}), 404
    if transaction.status == "pending":
        account_service.create_conflict(transaction_id)
        return jsonify({'message': 'transaction cancelled'}), 200

@jwt_required
@transaction_bp.route('/deposit', methods=['POST'])
def deposit_funds():
    user_id = user_authenticator.get_authenticated_user()
    amount = request.json.get('amount')
    if not amount:
        return jsonify({'message': 'amount is required'}), 400
    account_service.fund_account(user_id, amount)
    return jsonify({'message': 'account funded successfully'}), 200


@jwt_required
@transaction_bp.route('/withdraw', methods=['POST'])
def withdraw_funds():
    user_id = user_authenticator.get_authenticated_user()
    amount = request.json.get('amount')
    if not amount:
        return jsonify({'message': 'amount is required'}), 400
    account_service.withdraw_funds(user_id, amount)
    return jsonify({'message': 'amount succesfully withdrawn'}), 200

@jwt_required
@transaction_bp.route('/deleteTransaction', methods=['DELETE'])
def delete_transaction():
    transaction_id = request.json.get('transaction_id')
    transaction = transaction_service.get_transaction(transaction_id)
    if not transaction:
        return jsonify({'message': 'transaction not found'}), 404
    transaction_service.delete_transaction(transaction_id)
    return jsonify({'message': 'transaction deleted successfully'}), 200

@jwt_required
@transaction_bp.route('/update_transaction', methods=['PATCH'])
def update_transaction():
    transaction_id = request.json.get('transaction_id')
    transaction = transaction_service.get_transaction(transaction_id)
    if not transaction:
        return jsonify({'message': 'transaction not found'}), 404
    conflict = request.json.get('conflict')
    if not conflict:
        return jsonify({'message': 'amount is required'}), 400
    transaction_service.update_transaction(transaction_id, conflict=conflict)
    return jsonify({'message': 'transaction updated successfully'}), 200
