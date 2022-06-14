class ProblemSolve {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            int product = 1;
            int f = 0;
            for (int i = 0; i < nums.size(); i++) {
                product *= nums[i];
                if (nums[i] == 0)
                    f++;
            }

            if (f == nums.size())
                return nums;
            
            int productWoZero = 1;
            if (f > 1)
                productWoZero = 0;
            else {
                for (int i = 0; i < nums.size(); i++) {
                    if (nums[i] != 0)
                        productWoZero *= nums[i];
                }
            }

            for (int i = 0; i < nums.size(); i++) {
                if (nums[i] == 0)
                    nums[i] = productWoZero;
                else
                    nums[i] = product / nums[i];
            }

            return nums;
        }
};
