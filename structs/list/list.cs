using System;

namespace LinkedList
{
    public class Node{
        public int value;
        // reference to the next node in the list
        public Node next;
        // constructor
        public Node(int val) {
            value = val;
            next = null; //set the next node to be null
        }
        public void Print()
        {
            Console.Write("|" + value + "| -> ");
            if (next != null) {
                next.Print();
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Node myFirstNode = new Node(2);
            myFirstNode.next = new Node(5);
            myFirstNode.next.next = new Node(8);
            myFirstNode.next.next.next = new Node(0);
            myFirstNode.next.next.next.next = new Node(0);
            myFirstNode.next.next.next.next.next = new Node(1);
            myFirstNode.Print();
        }
    }

}