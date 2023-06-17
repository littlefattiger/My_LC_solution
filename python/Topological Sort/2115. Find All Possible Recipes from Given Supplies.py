# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        r_g = defaultdict()
        for i, v in enumerate(recipes):
            r_g[v] = ingredients[i]
        def helper(item, visited):
            if item   in supply_set:
                return True
            if item not in r_g:
                return False
            if item in visited:
                return False
            visited.add(item)
            for v in r_g[item]:
                if not helper(v, visited):
                    return False
            supply_set.add(item)
            visited.remove(item)     
            return True
        ans = []
        for v in recipes:
            if helper(v, set()):
                ans.append(v)
        return ans
