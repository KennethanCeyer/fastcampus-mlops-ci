<p align="center"><img height="90" src="./assets/logo.png" /></p>
<h1 align="center">FastCampus MLOps CI</h1>

## 소개

이 레포지토리는 CI(Continuous Integration) 구성의 이해를 돕기 위해 만들어졌습니다. 폴더 내의 구조는 다음과 같습니다.

```plaintext
fastcampus-mlops-ci/
├── README.md
├── app.py
├── assets
│   └── logo.png
├── ml_models
│   ├── __init__.py
│   └── xor.py
├── models
│   ├── __init__.py
│   └── xor.py
├── requirements.txt
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_app.py
├── trainer.py
└── xor_model.pth
```

## 설치

```bash
pip3 install -r requirements.txt
```

## 테스트

```bash
pytest tests/
```
