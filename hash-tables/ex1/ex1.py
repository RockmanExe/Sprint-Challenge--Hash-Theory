def get_indices_of_item_weights(weights, limit):
  # item_weights={}
  # difference= limit - weights
  # for i in range(len(weights)):
  #   if (difference) in item_weights:
  #     return (i, item_weights[difference])
  #   else:
  #     item_weights[weights[i]]= i

  weights_dict={}
  for i in range(len(weights)):
    weight = weights[i]
    if (limit - weight) in weights_dict:
      return (i, weights_dict[limit- weight])
    else:
      weights_dict[weights]= i
  return ()

get_indices_of_item_weights([4, 6, 10, 15, 16], 21 )

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 