import streamlit as st
import random
import time

# 초기 상태 설정
if 'question_idx' not in st.session_state:
    st.session_state.question_idx = 0
    st.session_state.score = 0
    st.session_state.questions = []
    st.session_state.finished = False

# 문제 생성
if len(st.session_state.questions) == 0:
    for _ in range(10):
        a, b = random.randint(2, 9), random.randint(2, 9)
        answer = a * b
        options = list(set([
            answer,
            answer + random.randint(1, 5),
            max(1, answer - random.randint(1, 5))
        ]))
        while len(options) < 3:
            options.append(random.randint(2, 81))
        random.shuffle(options)
        st.session_state.questions.append({
            'question': f"{a} × {b} = ?",
            'answer': answer,
            'options': options
        })

st.title("🎲 구구단 퀴즈")

if not st.session_state.finished:
    q_idx = st.session_state.question_idx
    question = st.session_state.questions[q_idx]

    st.subheader(f"문제 {q_idx + 1}/10")
    st.write(question['question'])

    selected = st.radio("보기 중 하나를 선택하세요:", question['options'], key=q_idx)

    if st.button("제출하기"):
        if selected == question['answer']:
            st.success("정답입니다! 🎉 빵빠레~🥳")
            st.balloons()
            time.sleep(1.5)  # 효과 감상 시간
            st.session_state.score += 1
            st.session_state.question_idx += 1
            if st.session_state.question_idx == 10:
                st.session_state.finished = True
            st.experimental_rerun()
        else:
            st.error("틀렸습니다! 다시 한 번 도전해보세요 💪")
else:
    st.success(f"퀴즈를 완료했습니다! 점수: {st.session_state.score}/10")
    st.balloons()
    st.info("수고 많았어요! 🎉 다시 도전해볼까요?")
    if st.button("처음으로 돌아가기"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
