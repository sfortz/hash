import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class Main {

    private static final String FILENAME = "src/test/a_example.in";
    private static final String FILEOUT = "src/test/solution.out";
    private static int numRides, numCol, numRows, fleet, bonus, steps;

    public static void main(String[] args) {

        ArrayList<Ride> initRides = importIn();
        Collections.sort(initRides);
        ArrayList<Ride> rides = repartition(initRides);
        ArrayList<Trajet> initTrajets = generateNextRides(rides);
        writer(initTrajets);

    }

    public static ArrayList<Ride> importIn() {

        ArrayList<Ride> rides = new ArrayList<Ride>();
        int i = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(FILENAME))) {

            String sCurrentLine = br.readLine();
            String[] tempInit = sCurrentLine.split(" ");
            numRows =  Integer.parseInt(tempInit[0]);
            numCol = Integer.parseInt(tempInit[1]);
            fleet = Integer.parseInt(tempInit[2]);
            numRides = Integer.parseInt(tempInit[3]);
            bonus = Integer.parseInt(tempInit[4]);
            steps = Integer.parseInt(tempInit[5]);

            while ((sCurrentLine = br.readLine()) != null) {
                //System.out.println(sCurrentLine);
                tempInit = sCurrentLine.split(" ");
                int RowStart  = Integer.parseInt(tempInit[0]);
                int ColumnStart = Integer.parseInt(tempInit[1]);
                int RowEnd  = Integer.parseInt(tempInit[2]);
                int ColumnEnd = Integer.parseInt(tempInit[3]);
                int earlStart = Integer.parseInt(tempInit[4]);
                int lateFinish = Integer.parseInt(tempInit[5]);
                rides.add(new Ride(i, ColumnStart, ColumnEnd, RowStart, RowEnd, earlStart, lateFinish));
                i++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return rides;
    }

    public static ArrayList<Ride> repartition(ArrayList<Ride> rides) {

        ArrayList<Ride> rideUnder5000 = rides.stream()
                .filter(r -> r.getLastStart() < 5000)
                .collect(Collectors.toCollection(ArrayList::new));

        return rideUnder5000;
    }

    public static int getValue(ArrayList<Trajet> trajets) {

        int val = 0;

        for(Trajet t: trajets){
            val += t.getVal(bonus);
        }

        return val;
    }


    public static void writer(ArrayList<Trajet> trajets){
        try{
            FileWriter fw = new FileWriter(FILEOUT);
            BufferedWriter buffer = new BufferedWriter(fw);
            PrintWriter file = new PrintWriter(buffer);
            for(int i=0; i<trajets.size(); i++){
                if(trajets.get(i) != null){
                    file.write(trajets.toString());
                }
                file.write("\n");
            }
            file.close();
        }catch(IOException e){
            System.out.println(e);
        }
    }

    //
    public ArrayList<Trajet> generateNextRide(ArrayList<Ride> rides,Trajet trajet){

        ArrayList<Trajet> trajets = new ArrayList<Trajet>();

        for (int i = 0; i < rides.size(); i++) {
            Trajet trajet2 = trajet.clone();
            trajet2.addRide(rides.get(i));
            trajets.add(trajet2);
        }


        return trajets;
    }
}