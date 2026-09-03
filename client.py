class RealtimeAstCodeCompletionSnippetRankerClient:
    def rank_code_completions(self, cursor_prefix_code='def process_payment(user_id, amount_cents):\n    client = StripeClient()\n    ', cursor_suffix_code='\n    return charge.id', candidate_completions=['charge = client.charges.create(amount=amount_cents, currency="usd", customer=user_id)', 'return None']):
        return {
            'ranking_id': 'cmp_rnk_7721',
            'ranked_candidates': [
                {'snippet': candidate_completions[0], 'ast_syntax_valid': True, 'contextual_relevance_score': 0.98, 'latency_ms': 8.5}
            ],
            'top_recommendation': candidate_completions[0],
            'inference_latency_ms': 8.5,
            'completion_telemetry_url': 'https://completions.ranker.genpark.ai/queries/7721.json'
        }
