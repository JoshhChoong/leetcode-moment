int maxProfit(int* prices, int pricesSize) {
    int ans = 0,bestAns;
    int h = 0, l = prices[0];
    int lPos = 0;

    for (int i = 0; i < pricesSize;i++){
        if (prices[i] < l){
            l = prices[i];
            h = 0;
            lPos = i;
        }  
        if (prices[i] > h && i > lPos){
            h = prices[i];
        }
        ans = h - l;
        if (ans > bestAns){
            bestAns = ans;
        }
    }
    return bestAns;
}