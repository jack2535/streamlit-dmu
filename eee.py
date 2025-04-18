import os
import tempfile
import whisper
import streamlit as st

# Whisper 모델 로드 (로컬)
def load_model():
    return whisper.load_model("base")  # 필요시 "small", "medium", "large" 가능

# 메인 처리
def transcribe_audio(audio_path):
    print(f"🎧 오디오 파일 처리 중: {audio_path}")
    result = model.transcribe(audio_path, language="ko")
    return result["text"]

# Streamlit 앱 설정
st.set_page_config(page_title="🎙️ AI 면접 분석기", layout="centered")
st.title("🎙️ STT-20231587김자호")
st.markdown("업로드된 오디오 파일을 Whisper로 로컬에서 텍스트로 변환한 뒤, 분석을 진행합니다.")

# 파일 업로드
audio_file = st.file_uploader("📁 인터뷰 음성 파일 업로드 (mp3)", type=["mp3"])

if audio_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    st.info("오디오 파일이 업로드되었습니다. STT 변환을 시작합니다...")

    try:
        # Whisper 모델 로딩
        model = load_model()

        # STT 변환
        full_transcript = transcribe_audio(tmp_path)

        st.success("🎧 STT 변환 완료!")

        # 텍스트 출력
        st.subheader("📝 전체 텍스트")
        st.text_area("변환된 텍스트", full_transcript, height=300)

    except Exception as e:
        st.error(f"오류 발생: {str(e)}")
    finally:
        os.unlink(tmp_path)
else:
    st.warning("오디오 파일을 업로드해 주세요.")