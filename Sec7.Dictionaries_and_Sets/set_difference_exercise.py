favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

# Add your code here.

# Create a sorted list called suggestions of customer's fav item wihtout any items in their basket
suggestions = sorted(favourites - basket)
print(suggestions)

