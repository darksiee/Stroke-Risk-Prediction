import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Tải mô hình
model = joblib.load("Stroke_Diagnosis_model.pkl")

def submit():
    try:
        # Lấy dữ liệu từ các ô nhập
        gender = int(gender_entry.get())
        age = float(age_entry.get())
        hypertension = int(hypertension_entry.get())
        heart_disease = int(heart_disease_entry.get())
        ever_married = int(ever_married_entry.get())
        work_type = int(work_type_entry.get())
        residence_type = int(residence_type_entry.get())
        avg_glucose_level = float(avg_glucose_entry.get())
        bmi = float(bmi_entry.get())
        smoking_status = int(smoking_status_entry.get())
        
        # Chuyển đổi dữ liệu thành DataFrame
        input_data = pd.DataFrame({
            'gender': [gender],
            'age': [age],
            'hypertension': [hypertension],
            'heart_disease': [heart_disease],
            'ever_married': [ever_married],
            'work_type': [work_type],
            'Residence_type': [residence_type],
            'avg_glucose_level': [avg_glucose_level],
            'bmi': [bmi],
            'smoking_status': [smoking_status]
        })

        # Dự đoán
        prediction = model.predict(input_data)

        # Hiển thị kết quả
        if prediction[0] == 1:
            messagebox.showinfo("Kết quả", "Người này có nguy cơ bị đột quỵ!")
        else:
            messagebox.showinfo("Kết quả", "Người này không có nguy cơ bị đột quỵ!")
    
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng cho tất cả các trường!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chẩn Đoán Người Mắc Bệnh Đột Quỵ")
root.geometry("600x800")  # width x heigh
root.configure(bg="#f2f2f2")  # Màu nền

# Thêm tiêu đề
title_label = tk.Label(root, text="Chẩn Đoán Bệnh Đột Quỵ", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
title_label.pack(pady=20)

# Thêm các ô nhập với padding
inputs = [
    ("Giới tính (0: Nam, 1: Nữ):", "gender"),
    ("Tuổi:", "age"),
    ("Bệnh cao huyết áp (0: Không, 1: Có):", "hypertension"),
    ("Bệnh tim (0: Không, 1: Có):", "heart_disease"),
    ("Tình trạng hôn nhân (0: Không, 1: Có):", "ever_married"),
    ("Loại hình công việc ('children':0,'Govt_job':1 ,'Private':2,'Self-employed':3, 'Never_worked':4):", "work_type"),
    ("Nơi cư trú (0: Nông thôn, 1: Thành phố):", "residence_type"),
    ("Mức glucose trung bình:", "avg_glucose"),
    ("Chỉ số BMI:", "bmi"),
    ("Tình trạng thuốc lá ('never smoked':1, 'formerly smoked':2 , 'smokes':3):", "smoking_status")
]

# Tạo các ô nhập
for label_text, entry_var in inputs:
    tk.Label(root, text=label_text, bg="#f2f2f2").pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(pady=5)
    globals()[f"{entry_var}_entry"] = entry

# Nút gửi dữ liệu
submit_button = tk.Button(root, text="Chẩn Đoán", command=submit, bg="#4CAF50", fg="white", font=("Helvetica", 12))
submit_button.pack(pady=20)

# Bắt đầu vòng lặp chính
root.mainloop()
