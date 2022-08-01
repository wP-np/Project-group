import api, cash_on_hand, overheads, profit_loss

def main():
    forex = api.api_function()
    cash_on_hand.coh_function(forex)
    overheads.overhead_function(forex)
    profit_loss.profitloss_function(forex)

main()

