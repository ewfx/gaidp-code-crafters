import pandas as pd
from datetime import datetime

def process_anomalies_dataset(csv_filepath):
    try:
        df = pd.read_csv(csv_filepath)
    except FileNotFoundError:
        return None

    df['ValidationMessages'] = ''

    for index, row in df.iterrows():
        messages = []

        if row['IdentifierType'] not in ["CUSIP", "ISIN", "SEDOL", "Internal"]:
            messages.append(f"IdentifierType is '{row['IdentifierType']}' which is not in ['CUSIP', 'ISIN', 'SEDOL', 'Internal']")

        if pd.isna(row['IdentifierValue']):
            messages.append("IdentifierValue is missing")

        try:
            cost = int(float(row['AmortizedCost_USDEquivalent']))
            if cost != round(cost):
                messages.append("AmortizedCost_USDEquivalent is not a rounded whole dollar amount")
        except (ValueError, TypeError):
            messages.append("AmortizedCost_USDEquivalent is missing or invalid")

        try:
            market_value = int(float(row['MarketValue_USDEquivalent']))
            if market_value != round(market_value):
                messages.append("MarketValue_USDEquivalent is not a rounded whole dollar amount")
        except (ValueError, TypeError):
            messages.append("MarketValue_USDEquivalent is missing or invalid")

        if row['AccountingIntent'] not in ["AFS", "HTM", "EQ"]:
            messages.append(f"AccountingIntent is '{row['AccountingIntent']}' which is not in ['AFS', 'HTM', 'EQ']")

        try:
            type_of_hedge = int(row['TypeOfHedge'])
            if type_of_hedge not in [1, 2]:
                messages.append(f"TypeOfHedge is {type_of_hedge} which is not in [1, 2]")
        except (ValueError, TypeError):
            messages.append("TypeOfHedge is missing or invalid")

        try:
            hedged_risk = int(row['HedgedRisk'])
            if hedged_risk not in [1, 2, 3, 4]:
                messages.append(f"HedgedRisk is {hedged_risk} which is not in [1, 2, 3, 4]")
        except (ValueError, TypeError):
            messages.append("HedgedRisk is missing or invalid")

        try:
            hedge_interest_rate = int(row['HedgeInterestRate'])
            if hedge_interest_rate not in [1, 2, 3, 4, 5]:
                messages.append(f"HedgeInterestRate is {hedge_interest_rate} which is not in [1, 2, 3, 4, 5]")
        except (ValueError, TypeError):
            messages.append("HedgeInterestRate is missing or invalid")

        try:
            hedge_percentage = float(row['HedgePercentage'])
            if hedge_percentage < 0 or hedge_percentage > 1:
                messages.append("HedgePercentage must be between 0 and 1")

        except (ValueError, TypeError):
            messages.append("HedgePercentage is missing or invalid")


        try:
            datetime.strptime(row['HedgeHorizon'], '%Y-%m-%d')
        except ValueError:
            messages.append("HedgeHorizon is not in yyyy-mm-dd format")
        except TypeError:
            messages.append("HedgeHorizon is missing or invalid")

        try:
            hedged_cash_flow = int(row['HedgedCashFlow'])
            if hedged_cash_flow not in [1,2]:
                messages.append(f"HedgedCashFlow is {hedged_cash_flow} which is not in [1,2]")

        except (ValueError, TypeError):
            messages.append("HedgedCashFlow is missing or invalid")


        try:
            sidedness = int(row['Sidedness'])
            if sidedness not in [1,2]:
                messages.append(f"Sidedness is {sidedness} which is not in [1,2]")
        except (ValueError, TypeError):
            messages.append("Sidedness is missing or invalid")


        try:
            hedging_instrument = int(float(row['HedgingInstrumentAtFairValue']))
            if hedging_instrument != round(hedging_instrument):
                messages.append("HedgingInstrumentAtFairValue is not a rounded whole dollar amount")
        except (ValueError, TypeError):
            messages.append("HedgingInstrumentAtFairValue is missing or invalid")

        try:
            effective_portion = int(float(row['EffectivePortionOfCumulativeGainsAndLosses']))
            if effective_portion != round(effective_portion):
                messages.append("EffectivePortionOfCumulativeGainsAndLosses is not a rounded whole dollar amount")
        except (ValueError, TypeError):
            messages.append("EffectivePortionOfCumulativeGainsAndLosses is missing or invalid")

        try:
            asu_designation = int(row['ASU2017-12HedgeDesignations'])
            if asu_designation not in [1, 2, 3]:
                messages.append(f"ASU2017-12HedgeDesignations is {asu_designation} which is not in [1, 2, 3]")
        except (ValueError, TypeError):
            messages.append("ASU2017-12HedgeDesignations is missing or invalid")

        df.loc[index, 'ValidationMessages'] = '\n'.join(messages)

    return df