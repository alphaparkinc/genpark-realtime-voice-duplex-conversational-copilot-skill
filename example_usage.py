from client import RealtimeVoiceDuplexConversationalCopilotClient

def main():
    client = RealtimeVoiceDuplexConversationalCopilotClient()
    res = client.process_duplex_audio("audio_raw_data_stream", "sess_9021")
    print(f"Streaming Latency: {res['latency_ms']}ms")
    print(f"User Interrupted: {res['user_interrupted']}")
    print(f"Response Audio Stream: {res['audio_response_stream']}")

if __name__ == "__main__":
    main()
