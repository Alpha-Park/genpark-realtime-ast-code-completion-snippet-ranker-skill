from client import RealtimeAstCodeCompletionSnippetRankerClient

def main():
    client = RealtimeAstCodeCompletionSnippetRankerClient()
    res = client.rank_code_completions('def add(a, b): ', '')
    print('AST Completion Snippet Ranker: ' + res['ranking_id'] + ' (Latency: ' + str(res['inference_latency_ms']) + 'ms)')
    print('Top Completion: "' + res['top_recommendation'] + '"')
    print('Telemetry URL: ' + res['completion_telemetry_url'])

if __name__ == '__main__':
    main()
