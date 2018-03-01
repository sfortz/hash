public class Ride implements Comparable{

	int id;
	int ColumnStart;
	int ColumnEnd;
	int RowStart;
	int RowEnd;
	int earlStart;
	int lateFinish;

	public Ride(int id, int ColumnStart,int ColumnEnd,int RowStart,	int RowEnd, int earlStart, int lateFinish) {
		this.id = id;
		this.ColumnStart = ColumnStart;
		this.ColumnEnd = ColumnEnd;
		this.RowStart = RowStart;
		this.RowEnd = RowEnd;
	}

	public int getDistance() {
		return Math.abs(ColumnStart - ColumnEnd) + Math.abs(RowEnd-RowStart);
	}

	public int getLastStart() {
		return this.lateFinish - this.getDistance();
	}

	@Override public int compareTo(Object o){
		Ride i = (Ride) o;
		if(this.getLastStart() < i.getLastStart())
			return -1;

		if(this.getLastStart() > i.getLastStart())
			return 1;

		return 0;
	}
	
}
