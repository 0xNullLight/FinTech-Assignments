# Module 1 - Case Study

![Teller Protocol](https://pbs.twimg.com/profile_banners/1211074807975907328/1699023894/1500x500)

Teller Finance was founded in 2020 by Ryan Berkun. The company is headquartered in San Francisco, California.

~~Originally, the idea of **Teller Protocol** is to be able to connect to your bank account via plaid & complete other task such as what's shown within this~~ [old video](https://youtu.be/vGSpfIr6Cms).
~~But due to the nature of crypto, defi and changes within the market, currently, they have moved away from plans on v1.~~

~~**For the whitepaper for v1:**~~

~~https://teller-hosting.s3-us-west-1.amazonaws.com/Teller+Protocol+V1.0+Whitepaper.pdf~~

# [Teller Lite (v2)](https://docs.teller.org/teller-lite/) (Ethereum, Polygon, Arbitrum One, Base, Mantle)

Imagine **Peer-to-peer lending (p2p)** on the Blockchain. Imagine the next evolution of **defi lending protocols** where you're **no longer bounded by price-based liquidation**.
This is what Teller Protocol offers.
**_As of date, their is no token offered by this protocol as discussed in that old youtube video I provided._**


In the world of defi, some of the most popular **lending & borrowing protocols** (ex: **Aave**) tend to be acompany by **price-based** liquidation pools via the help of **Oracles** such as **ChainLink** meant to help pull in real-world data to talk to on-chain data.

**Teller protocol** changes that by **replacing price-based liquidation pools with a time-based liquidation pool** allowing **fixed collateral, fixed duration loans** in concentrated liquidity order-books.

## What are Time-Based Liquidation?
Loans are only vulnerable to liquidation if a borrower fails to make a scheduled repayment. Unlike **price-based** liquidation pools that rely on health factors or other collateral factors, any change in the underlying value of the collateral does not trigger liquidation on Teller. If a borrower doesn’t make a scheduled repayment after a pre-determined due date (plus a grace period), the loan will default.

Utilizing the Teller Protocol, because their is no oracle involved where data from the real-world could interact with the blockchain causing possible liquidation, what happens is that when a loan is made, the lender gets to set the conditions of when a loan should be paid or extended by. As long as the interest of the loan gets paid and their is enough liquidity, you can theoretically keep extending and paying the loan payment period endlessly without the worry of the loan being liquidated because of price.

## Examples and differences between Price-Based vs Time-Based liquidation

Imagine this scenerio..

You have an asset, let's call it **Asset A**. This is your collateral.
We want to borrow against it to obtain **Asset B**.

In a typical **price-based liquidation** borrow/lending protocol, if you were to borrow **ASSET B** against **ASSET A**. If **ASSET A** drops in price value based off the data obtain from the oracle, it could cause for a liqudation in which you lose your entire position.

In a **time-based liquidation** borrow/lending protocol such as **Teller Protocol**, if you were to borrow **ASSET B** against **ASSET A**. If **ASSET A** drops in price value. _**It wouldn't matter**_ because their is no oracle involved where real-world data would be taken into consideration possibly affecting liquidation. The only thing that matters is that you pay back on time.

## The bottom line to keep note of when borrowing/lending is..

Their are many defi protocol borrowing/lending strategies, but it all stems down to this..

**"Lenders get APY or the Collateral (if borrow defaults or get liquidated), Borrowers get liquidity and terms (duration of the loan)"**

## Things to consider

Utilizing **Cred Score** & **Spectral Score** to measure the defi eqvaulient of a credit score for a particular crypto wallet; Teller Protocol can help defi users determine the trust worthiness of a particular crypto wallet.

Email requirement for **"Custom loan"** feature has been fixed, email is optional for loan requests! 

You can rollover any loan indefinitely with **Extensions**. As long as there is a standing offer, you can "refinance" and extend your loan indefinitely. 

## Important note:

Anybody whom wants to, can find a defaulted loan or a loan that is soon to be put up for liqudation & offer to pay off that loan in exchange to redeem the collateral used within that speicific loan; in a sense becoming a crypto debt collector within the realms of defi.

## Active Liquidity Pools

**Example of Current Active LP For ETH**:
![Teller's LP (ETH)]([[https://raw.githubusercontent.com/Hcrypt/FinTech-Assignments/main/Teller_Active_Pool_as_of_11182023_(ETH).png?token=](https://github.com/Hcrypt/FinTech-Assignments/blob/main/Teller_Active_Pool_as_of_11182023_(ETH).png?raw=true)](https://raw.githubusercontent.com/Hcrypt/FinTech-Assignments/main/Teller_Active_Pool_as_of_11182023_(ETH).png?token=GHSAT0AAAAAACKNCWHJDDGKX3NICZBHUQYSZK36BQQ))

**Total volume:**  
The aggregate amount of funds or assets currently present in the liquidity pools. This represents the total value of assets that are available for lending and borrowing within the protocol.

**Total available:**  
The amount of funds or assets that are currently available for borrowing from the liquidity pools. It represents the portion of the total pool volume that is not currently borrowed and is accessible for users to borrow.

**Total borrowed:**  
The sum of funds or assets that have been borrowed from the liquidity pools. This value represents the amount of assets that have been utilized by borrowers from the available liquidity pools.

**1) Ethereum**  
https://app.teller.org/polygon/pools/address/0x

**2) Polygon**  
https://app.teller.org/polygon/pools/address/0x

**3) Arbitrum One**  
https://app.teller.org/arbitrum-one/pools/address/0x

**4) Base**  
https://app.teller.org/base/pools/address/0x

**5) Mantle**  
https://app.teller.org/mantle/pools/address/0x

## Deployed Contracts

| Name | Address (ETH) | Address (Polygon) | Address (Arbitrum One) |
| ----- | ----- | ----- | ----- |
| TellerV2 | 0x00182FdB0B880eE24D428e3Cc39383717677C37e | 0xD3D79A066F2cD471841C047D372F218252Dbf8Ed | 0x5cfD3aeD08a444Be32839bD911Ebecd688861164 |
| Reputation Manager | 0xF0da18a5b53a6C0c4e763013A8DAEeD895A93627 | 0xb129444b90fc2646f5f3b514c5cd3fafd43f071a | 0xa8eC4511C5f7E8B0859b1e3BFF50641ecf98f30B |
| Market Registry | 0x5e30357d5136Bc4BfaDBA1ab341D0da09Fe7a9F1 | 0xef0f89bac623ed7c875bc2f23b5403dcf90ba8bd | 0x2bD9697bF0AB44bE5cA698fB5787d8F13ca48Ffc |
| Lender Manager | 0xdbb554e621e1cc52d9ad63b6e47fc98568264115 | 0x8199dc6d35275f998aa459b29d642577818e9d3e | 0x5594f9EE0DdF1e2D21ac8125dfeA66fc4c85Cd01 |
| Lender Commitment Forwarder | 0x17A8e82351661DFD568FEE6D7c38695b67e1e924 | 0x84B550EE6959FA3F3A44498836F2A9473734ba78 | 0x84B550EE6959FA3F3A44498836F2A9473734ba78 |
| Proxy Admin | 0x4d41AA4BdE441A5A4477f307FC1Da20Ee2615F66 | 0x663ce382c4d169cea8b1eff7adaa973560054937 | 0xD9149bfBfB29cC175041937eF8161600b464051B |
| Collateral Manager | 0x2551A099129ad9b0b1FEc16f34D9CB73c237be8b | 0x76888a882a4ff57455b5e74b791dd19df3ba51bb | 0x71B04a8569914bCb99D5F95644CF6b089c826024 |
| Collateral Escrow Beacon | 0xfa0a79661ad21fbd416ddbD9a098564b3686adf5 | 0xac2000e8a637656c39aa7a61497b2d32d74758a4 | 0x86D540Ca6de284c18BeED0F6f154499CF9b61322 |
| Collateral Escrow | 0x27f57e6E919EB8fa8EA8f64a45dD425C70d3Ad44 | 0x7d7836b03358c0828cf2f5d6f8140c122679b7d0 | 0xfF5c6530d761aB1Fa5E78e70C791A260Cfe85FbC |

| Name | Address (Base) | Address (Mantle)
| ----- | ----- | ----- |
| TellerV2 | 0x5cfD3aeD08a444Be32839bD911Ebecd688861164 | 0xe6774DAAEdf6e95b222CD3dE09456ec0a46672C4 |
| Reputation Manager | 0xa8eC4511C5f7E8B0859b1e3BFF50641ecf98f30B | 0x88F8c9e7dACC43Aa37C45C4FfAA204fda821704c |
| Market Registry | 0x2bD9697bF0AB44bE5cA698fB5787d8F13ca48Ffc | 0x5Bb23271A93433B13c13D19826bc155a00694B2E |
| Lender Manager | 0x5594f9EE0DdF1e2D21ac8125dfeA66fc4c85Cd01 | 0xD6489a0021ca74DAAf3d70aD26FD4E92aB1b0797 |
| Lender Commitment Forwarder | 0x84B550EE6959FA3F3A44498836F2A9473734ba78 | 0x1E36C7e9fDa74e84eA3F21F733C93903637601b3 |
| Proxy Admin | 0x001F15eF4a2Feb778823952af512F717811E4456 | 0x001F15eF4a2Feb778823952af512F717811E4456
| Collateral Manager | 0x71B04a8569914bCb99D5F95644CF6b089c826024 | 0x6eB9b34913Bd96CA2695519eD0F8B8752d43FD2b |
| Collateral Escrow Beacon | 0x86D540Ca6de284c18BeED0F6f154499CF9b61322 | 0x86D540Ca6de284c18BeED0F6f154499CF9b61322 |
| Collateral Escrow | 0xfF5c6530d761aB1Fa5E78e70C791A260Cfe85FbC | 0xfF5c6530d761aB1Fa5E78e70C791A260Cfe85FbC |


https://docs.teller.org/v2/resources/deployed-contracts




## Links

1) [Official Website](https://teller.org/)
2) [Teller Blog](https://blog.teller.org/)
3) [Fortune Teller NFT](https://teller-finance.notion.site/Fortune-Teller-NFTx-Pools-2c4d14457e6f4983bd60cb2fbab8c4e6)
4) [Teller Protocol's GitHub](https://github.com/teller-protocol)
5) [Teller Lite (v2) GitBook](https://docs.teller.org/teller-lite/)
6) [Teller (v2) Advance GitBook](https://docs.teller.org/v2/)
