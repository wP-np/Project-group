import api, cash_on_hand, overheads, profit_loss


forex = api.api_function()

print(cash_on_hand.coh_function(forex))
print(overheads.overhead_function(forex))
print(profit_loss.profitloss_function(forex))

