public class Main{
    public static void main(String[] args){
        long[] g = new long[]{2,4,6,8,10,12,14,16};
        double[] x = new double[10];
        for(int i=0;i<10;i++){
            x[i] = (Math.random()*22.0)-15.0;
        }
        double[][]p = new double[8][10];
        for(int i=0;i<8;i++){
            for(int j=0;j<10;j++){
                if (g[i] == 6){
                    p[i][j] = Math.log(Math.pow(Math.E, Math.cos(Math.tan(x[j]))));
                }
                else if (g[i]==2 || g[i]==10 || g[i]==14 || g[i]==16){
                    p[i][j] = Math.pow((3.0/4.0) / (Math.cbrt(Math.tan(x[j]))), 2);
                }
                else{
                    p[i][j] = Math.atan(Math.pow(1.0 / (Math.pow(Math.E,Math.abs(x[j]))), 4));
                }
            }
        }
        
        printMatrix(p);
        
    }
    public static void printMatrix(double[][] mat){
        for(int i=0;i<8;i++){

            for(int j=0;j<10;j++){
                if (mat[i][j]<0 || mat[i][j]>10){
                System.out.printf("%.2f  ", mat[i][j]);
                }
                else{
                    System.out.printf(" %.2f  ", mat[i][j]);
                }
            }
            System.out.println();
    }}


}