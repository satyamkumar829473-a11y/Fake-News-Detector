# 📰 Fake News Detector 
A simple web-based Fake News Detection system built using **Python**, **Flask**, **HTML**, and **CSS**. The application compares user-entered news with news stored in a CSV dataset and determines whether the news is available in the dataset. 

## 🚀 Features 
- User-friendly web interface
- Detects news using CSV dataset comparison
- Displays matching news results
- Shows "No News Available" when no match is found
- Lightweight and easy to run

## 🛠️ Technologies Used 
- Python
- Flask
- HTML5
- CSS3
- CSV Dataset

## 📂 Project Structure 
Fake-News-Detector/ 
├── app.py 
├── news.csv
├── README.md 
├── templates/
|      └── index.html 
├── static/
│      └── style.css 
│      └── download3.jpg 
└── screenshots/

## ⚙️ Installation 
1. Clone the repository```bash git clone https://github.com/satyamkumar829473-a11y/Fake-News-Detector.git 
2. Move to project directory
- cd Fake-News-Detector 
3. Install dependencies
- pip install flask pandas 
4. Run the application
- python app.py 
5. Open browser and visit
- http://127.0.0.1:5000 

## 📖 How It Works
- User enters a news headline.
- The application reads data from news.csv.
- The entered news is compared with the dataset.
- If a match is found, the news is displayed.
- If no match is found, the application displays:
- No News Available 

## 📊 Dataset
The project uses a CSV file (news.csv) containing news headlines and related information for comparison.

## 🔮 Future Improvements
- Machine Learning based fake news detection
- Real-time news verification
- News confidence score
- API integration for live news checking
- NLP-based text similarity matching

## 👨‍💻 Author
Satyam Kumar

## 📜 License
This project is developed for educational and learning purposes.
