public class Trajet {

    private int van, posDepX, posDepY, posEndX, posEndY, timeDep, timeEnd;
    private Ride[] rides;

    public Trajet(int van, int posDepX, int posDepY, int posEndX, int posEndY, int timeDep, int timeEnd, Ride[] rides) {
        this.rides = rides;
        this.posDepX = posDepX;
        this.posDepY = posDepY;
        this.posEndX = posEndX;
        this.posEndY = posEndY;
        this.timeDep = timeDep;
        this.timeEnd = timeEnd;
        this.van = van;
    }

    @Override
    public String toString(){

        String str = "";

        for (Ride r: rides){
            str= str + " " + r.id;
        };

        str = rides.length + str + "\n";
        return str;
    }
}
