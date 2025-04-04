{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fb151c2a-ae59-438f-8707-2f0ac4ca04ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-05 01:40:33.089 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.090 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.091 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.091 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.091 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.092 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.092 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.092 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.092 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.094 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.094 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.094 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.094 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.095 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.095 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.095 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.095 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.096 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.097 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.097 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-05 01:40:33.098 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import pandas as pd\n",
    "\n",
    "# Load the trained model\n",
    "with open(\"fire_model.pkl\", \"rb\") as model_file:\n",
    "    model = pickle.load(model_file)\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"🔥 Fire Risk Prediction App\")\n",
    "\n",
    "# User inputs for prediction\n",
    "TMP_sfc = st.number_input(\"Enter Temperature (TMP_sfc)\", min_value=-50.0, max_value=50.0, value=25.0)\n",
    "RH_2m = st.number_input(\"Enter Relative Humidity (RH_2m)\", min_value=0.0, max_value=100.0, value=50.0)\n",
    "APCP_sfc = st.number_input(\"Enter Precipitation (APCP_sfc)\", min_value=0.0, max_value=500.0, value=10.0)\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict Fire Risk\"):\n",
    "    # Create input DataFrame\n",
    "    input_data = pd.DataFrame([[TMP_sfc, RH_2m, APCP_sfc]], columns=['TMP_sfc', 'RH_2m', 'APCP_sfc'])\n",
    "    \n",
    "    # Make prediction\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    \n",
    "    # Display result\n",
    "    if prediction == 1:\n",
    "        st.error(\"🔥 High Fire Risk Detected!\")\n",
    "    else:\n",
    "        st.success(\"✅ Low Fire Risk\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cea0f21b-9ab5-43f1-a472-75b8c42fbb31",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4aa4718-5bdc-46fb-b9a2-c99a12d39219",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
