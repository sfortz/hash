import java.util.ArrayList;


public class Trajet implements Comparable{

    private int van, posDepX, posDepY, posEndX, posEndY, timeDep, timeEnd, bonus;
    private ArrayList<Ride> rides;

    public Trajet(int van, int posDepX, int posDepY, int posEndX, int posEndY, int timeDep, int timeEnd) {
        this.posDepX = posDepX;
        this.posDepY = posDepY;
        this.posEndX = posEndX;
        this.posEndY = posEndY;
        this.timeDep = timeDep;
        this.timeEnd = timeEnd;
        this.van = van;
    }

    public int getVal(int bonus){
        this.bonus = bonus;
        int sum = 0;
        int curTime = 0;
        for (Ride r: this.rides){
            sum+= r.getDistance();
            if(r.getEarlStart()==curTime){
                sum += bonus;
            }
            curTime += r.getDistance();
        }
        return sum;
    }

    @Override
    public String toString(){

        String str = "";

        for (Ride r: rides){
            str= str + " " + r.id;
        };

        str = rides.size() + str + "\n";
        return str;
    }

    public void addRide(Ride newRide){
        rides.add(newRide);
    }

    public Trajet clone(){
        return new Trajet( van,  posDepX,  posDepY,  posEndX,  posEndY,  timeDep,  timeEnd);
    }

    @Override
    public int compareTo(Object o){
        Trajet i = (Trajet) o;
        if(this.getVal(bonus) < i.getVal(bonus))
            return -1;

        if(this.getVal(bonus) > i.getVal(bonus))
            return 1;

        return 0;
    }
}
