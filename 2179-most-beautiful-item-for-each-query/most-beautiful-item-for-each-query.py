class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        output = []
        price_max_beauty_dict = {}
        
        # Step 1: Sort items by price
        items = sorted(items)
        
        # Step 2: Build a price -> max beauty mapping
        previous_max = 0
        for price, beauty in items:
            max_val = max(previous_max, beauty)
            price_max_beauty_dict[price] = max_val
            previous_max = max_val
        
        print("Price to max beauty map:", price_max_beauty_dict)

        # Step 3: Sort prices and queries
        sorted_prices = list(price_max_beauty_dict.keys())
        sorted_queries = sorted(queries)
        
        # Step 4: Use two-pointer technique to find the result for each query
        previous_index = 0
        query_results = {}
        
        for q in sorted_queries:
            # If query exceeds the max price, take the max beauty at the last price
            if q > sorted_prices[-1]:
                query_results[q] = price_max_beauty_dict[sorted_prices[-1]]
                continue
            
            # Move the pointer to find the largest price <= q
            while previous_index < len(sorted_prices) and sorted_prices[previous_index] <= q:
                previous_index += 1
            
            # The corresponding max beauty is at previous_index - 1
            if previous_index > 0:
                query_results[q] = price_max_beauty_dict[sorted_prices[previous_index - 1]]
            else:
                query_results[q] = 0  # If no price <= q exists

        # Preserve the original order of queries
        for q in queries:
            output.append(query_results[q])

        return output
