int product[] = new int[nums.length];
product[0] = 1;
int sp = 1;

for (int i = 1; i < nums.length; i++) {
    product[i] = nums[i - 1] * product[i - 1];
}
for (int i = nums.length - 1; i >= 0; i--) {
    product[i] = sp * product[i];
    sp = sp * nums[i];
}

return product;