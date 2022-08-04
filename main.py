import api, cash_on_hand, overheads, profit_loss

def main():
    """
    The function will call the other respective functions providing the functions with its parameter (Conversion rate) and runs all the 
    functions at once
    """
    forex = api.api_function()
    cash_on_hand.coh_function(forex)
    overheads.overhead_function(forex)
    profit_loss.profitloss_function(forex)

main()