# Wallet operations: UTXOs, dust, consolidation, and addresses

A wallet tracks unspent transaction outputs. Spending many small inputs can require more transaction data and higher fees.

Protocol dust and an output that is merely uneconomic to spend at current fees are not the same thing.

Austin's 0.01 to 0.02 BTC transfer threshold is a rule of thumb, not a Bitcoin rule. Check current fees, exchange exposure, withdrawal costs, and the future spend fee.

Consolidation can reduce future input count but creates a transaction now and can link coins, reducing privacy. Use fresh receive addresses and verify the destination on the hardware display.

Coin control can affect privacy, change, fees, and tax identification. Use it only with matching records made no later than the transaction.

**Complete when:** the transfer threshold and any consolidation decision are tied to current fees, counterparty exposure, and a stated privacy trade-off.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
