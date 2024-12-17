int maxProfit(int* prices, int pricesSize) {
    int l = 0,r = 0;
    int bestAns = 0, ans;
    while (r < pricesSize - 1){
        r ++;
        ans = prices[r] - prices[l];
        if (ans > 0){
            if (ans > bestAns){
                bestAns = ans;
            }
        }else if (ans < 0 ) {
            l = r;
        }
    }
    return bestAns;
} 