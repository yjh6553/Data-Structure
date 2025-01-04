class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort the product list lexicographically
        products.sort()
        result = []
        prefix = ""
        
        for char in searchWord:
            prefix += char  # Incrementally build the prefix
            # Use binary search to find the start of matching products
            start_index = bisect.bisect_left(products, prefix)
            
            # Collect up to three matching products
            suggestions = []
            for i in range(start_index, min(start_index + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            result.append(suggestions)
        
        return result