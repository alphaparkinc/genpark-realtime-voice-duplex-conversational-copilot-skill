class RealtimeVoiceDuplexConversationalCopilotClient:
    def process_duplex_audio(self, audio_chunk_base64: str, session_id: str = "sess_voice_101") -> dict:
        return {
            "audio_response_stream": "https://stream.example.com/audio/duplex_resp.aac",
            "user_interrupted": False,
            "latency_ms": 95
        }
