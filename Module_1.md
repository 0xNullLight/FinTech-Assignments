
# Module 1 - Case Study

![Teller Protocol](https://pbs.twimg.com/profile_banners/1211074807975907328/1699023894/1500x500)

Teller Finance was founded in 2020 by Ryan Berkun. The company is headquartered in San Francisco, California.

~~Originally, the idea of **Teller Protocol** is to be able to connect to your bank account via plaid & complete other task such as what's shown within this~~ [old video](https://youtu.be/vGSpfIr6Cms).
~~But due to the nature of crypto, defi and changes within the market, currently, they have moved away from plans on v1.~~

~~**For the whitepaper for v1:**~~

~~https://teller-hosting.s3-us-west-1.amazonaws.com/Teller+Protocol+V1.0+Whitepaper.pdf~~

# [Teller Lite](https://docs.teller.org/teller-lite/) (Ethereum, Polygon, Arbitrum One, Base, Mantle)

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

**"Lenders get APY or the Collateral, Borrowers get liquidity and short terms"**

## Things to consider

Utilizing **Cred Score** & **Spectral Score** to measure the defi eqvaulient of a credit score for a particular crypto wallet; Teller Protocol can help defi users determine the trust worthiness of a particular crypto wallet.

Email requirement for **"Custom loan"** feature has been fixed, email is optional for loan requests! 

You can rollover any loan indefinitely with **Extensions**. As long as there is a standing offer, you can "refinance" and extend your loan indefinitely. 

## Important note:

Anybody whom wants to, can find a defaulted loan or a loan that is soon to be put up for liqudation & offer to pay off that loan in exchange to redeem the collateral used within that speicific loan; in a sense becoming a crypto debt collector within the realms of defi.

## Links

1) [Official Website](https://teller.org/)
2) [Teller Blog](https://blog.teller.org/)
3) [Fortune Teller NFT](https://teller-finance.notion.site/Fortune-Teller-NFTx-Pools-2c4d14457e6f4983bd60cb2fbab8c4e6)
4) [Teller Protocol's GitHub](https://github.com/teller-protocol)
