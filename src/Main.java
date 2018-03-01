import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    private static final String FILENAME = "src/test/a_example.in";
    private static final String FILEOUT = "src/test/solution.out";
    private static int numRides, numCol, numRows, fleet, bonus, steps;

    public static void main(String[] args) {

        ArrayList<Ride> initRides = importIn();
        Collections.sort(initRides);
        ArrayList<Trajet> initTrajets = repartition(initRides);
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

    public static ArrayList<Trajet> repartition(ArrayList<Ride> rides) {
        ArrayList<Trajet> trajets = new ArrayList<>();

        //Stream<Ride> rideUnder5000 = rides.stream().filter(r -> r.getLastStart() < 5000);
        List<Ride> rideUnder5000 = rides.stream()
                .filter(r -> r.getLastStart() < 5000)
                .collect(Collectors.toCollection(ArrayList::new));

        return  trajets;
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
}