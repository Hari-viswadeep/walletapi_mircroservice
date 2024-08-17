from flask import request
from flask_restx import Resource, abort, Namespace

from wallet import wallet, InsufficientAmount

ns_wallet = Namespace('wallet', 'Endpoints for managing a wallet balance')

@ns_wallet.route("/")
class Wallet(Resource):
    def post(self):
        # Load and validate request payload.
        result = request.get_json()
        # Return results
        return result

    def get(self):
        return "Wallet contains {}".format(wallet)

@ns_wallet.route("/addfund/<amount>")
class AddCash(Resource):
    def post(self,amount):
        wallet.add_cash(float(amount))
        return f"Wallet now contains {wallet.balance}"

@ns_wallet.route("/removefund/<amount>")
class SpendCash(Resource):
    def post(self,amount):
        wallet.spend_cash(float(amount))
        return f"Wallet now contains {wallet.balance}"
