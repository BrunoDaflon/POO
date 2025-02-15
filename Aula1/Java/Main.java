package Java;

class Pessoa {
    String nome;
    String sobrenome;
    int idade; 
    String cpf;

    public Pessoa(String nome, String sobrenome, int idade, String cpf) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.idade = idade;
        this.cpf = cpf;
    }
}

public class Main {

    public static void main(String[] args) {
        Pessoa pessoa1 = new Pessoa("Ze", "das Coves", 40, "1234567800");
        System.out.println("O nome e: "+pessoa1.nome+" "+pessoa1.sobrenome);
    }
}