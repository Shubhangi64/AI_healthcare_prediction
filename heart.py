import numpy as np
import pickle

# loading the saved model
model_2 = pickle.load(open('H:\\internshala course (python programming)\\health project\\heart_model.sav', 'rb'))


# input_data = (53,1,2,130,197,1,0,152,0,1.2,0,0,2)

# # changing the input_data to numpy array
# input_data_as_numpy_array = np.asarray(input_data)

# # reshape the array as we are predicting for one instance
# input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# prediction = load_model.predict(input_data_reshaped)
# print(prediction)

# if (prediction[0] == 0):
#   print('The person is not having heart disease')
# else:
#   print('The person is having heart disease')


  
def heart_disease_prediction(inputs_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(inputs_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    predictions = model_2.predict(input_data_reshaped)
    print(predictions)

    if (predictions[0] == 0):
      return 'The person is not having heart disease'
    else:
      return 'The person is having heart disease'
    





# h= heart_disease_prediction([59,1,0,140,177,0,1,162,1,0,2,1,3])
# print(h)