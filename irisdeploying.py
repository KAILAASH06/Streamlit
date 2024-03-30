import streamlit as st
import pickle



def get_Id():
    Id = st.text_input("Id of Iris")
    return Id

def get_Sepal_Length():
    Sepal_Length = st.text_input("SepalLength of Iris")
    return Sepal_Length

def get_Sepal_Width():
    Sepal_Width = st.text_input("SepalWidth of Iris")
    return Sepal_Width

def get_Petal_Length():
    Petal_Length = st.text_input("PetalLength")
    return Petal_Length

def get_Petal_Width():
    Petal_Width = st.text_input("PetalWidth of Iris")
    return Petal_Width

def predict_species(id,sl,sw,pl,pw):
    loaded_model = pickle.load(open('decision_tree_model (3).pkl','rb'))
    new_data = [[float(id),float(sl),float(sw),float(pl),float(pw),]]
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data: ")
    st.write(prediction)




if __name__ == "__main__":
    st.title('Iris Species prediction with Decision Tree model')
    st.image('iris.jpg')
    Id = get_Id()
    Sepal_Length = get_SepalLength()
    Sepal_Width = get_SepalWidth()
    Petal_Length = get_PetalLength()
    Petal_Width=get_PetalWidth()
    st.write("The parameters you entered are: ")
    st.write("Id", Id)
    st.write("Sepal length ", Sepal_Length)
    st.write("Sepal Width ", Sepal_Width)
    st.write("Petal length ", Petal_Length)
    st.write("Petal Width ", Petal_Width)


if st.button("Predict"):
    predict_species(Id,Sepal_Length,Sepal_Width,Petal_Length,Petal_Width)

