class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions=sorted(potions)
        pairs = []
        
        for spell in spells:
            required_potion = (success + spell - 1) // spell
            low = 0
            high = len(potions)
            best_index = high
            
            while low < high:
                mid = low + (high - low) // 2
                
                if potions[mid] >= required_potion:
                    best_index = mid
                    high = mid
                else:
                    low = mid + 1
            successful_count = len(potions) - best_index
            pairs.append(successful_count)
            
        return pairs
        