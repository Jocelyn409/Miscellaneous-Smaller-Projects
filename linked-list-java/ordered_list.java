import java.io.FileNotFoundException;
import java.util.Iterator;
import java.lang.Iterable;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

public class OrderedList implements Iterable<String> {
    private Node head;

    public Iterator<String> iterator() {
        return new LLIterator();
    }

    private class LLIterator implements Iterator<String> {
        private Node current = head;

        public boolean hasNext() {
            return current != null;
        }

        public String next() {
            String item = current.data;
            current = current.next;
            return item;
        }

        public void remove() {}
    }

    private class Node {
        private String data;
        private Node next;

        private Node(String item) {
            data = item;
            next = null;
        }
    }

    public OrderedList () {
        head = null;
    }

    public void insert(String item) {
        Node n = new Node(item);
        Node cur = head, back = null;

        while(cur != null) {
            if(cur.data.equals(item)) {
                return;
            }
            if(cur.data.compareTo(item) < 0) {
                back = cur;
                cur = cur.next;
            }
            else
                break;
        }

        if(back == null) {
            head = n;
        }
        else {
            back.next = n;
        }
        n.next = cur;
    }

    public void delete(String item) {
        Node cur = head, back = null;

        while (cur != null) {
            if (cur.data.equals(item)) {
                if (back == null) {
                    head = cur.next;
                }
                else {
                    back.next = cur.next;
                }

                break;
            } else {
                back = cur;
                cur = cur.next;
            }
        }
    }

    public static void dumplist(OrderedList oL) {
        for(String i : oL)
            System.out.println(i);
    }

    public static void main(String[] args) throws FileNotFoundException {

        Scanner dat = new Scanner(new FileReader(args[0]));
        Scanner delete = new Scanner(new FileReader(args[1]));
        PrintWriter output = new PrintWriter(args[2]);

        OrderedList list = new OrderedList();

        String y;

        while(dat.hasNext()) {
            y = dat.next();
            list.insert(y);
        }

        while(delete.hasNext()) {
            y = delete.next();
            list.delete(y);
        }

        for(String out : list)
            output.println(out);

        //dumplist(list);

        dat.close();
        delete.close();
        output.close();
    }

}
