from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/')
def route_default():
    return 'Welcome to my pageeee'

@app.route('/blockchain')
def route_blockchain():
    result = blockchain.to_json()
    return jsonify(result)

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)

    return jsonify(blockchain.chain[-1].to_json())

app.run()