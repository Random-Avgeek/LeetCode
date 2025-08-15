class Solution {
    public int countPrimes(int n) {
        int count=0;
        boolean[] isPrime = new boolean[n + 1];
        if(n==0){
            return 0;
        }
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i<n; i++){
            isPrime[i]=true;
        }
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        for (int i=2; i<=n; i++){
            if (isPrime[i]==true){
                count++;
            }
        }
        return count;
    }
}