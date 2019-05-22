var count = 1;
var countCorrect = 0;
var waitingForNext = false;

var title = document.getElementById("title");
var question = document.getElementById("question");
var option1 = document.getElementById("option1");
var option2 = document.getElementById("option2");
var option3 = document.getElementById("option3");
var option4 = document.getElementById("option4");
var option5 = document.getElementById("option5");

var card = document.getElementById("card");
var next = document.getElementById("next");
var buttons = document.getElementById("buttons");

function assignNextQuestion() {
    if (data_from_django.length < count)
        return;

    next.remove();
    
    option1.classList.remove("btn-success", "btn-danger", "active");
    option1.classList.add("btn-primary");
    option2.classList.remove("btn-success", "btn-danger", "active");
    option2.classList.add("btn-primary");
    option3.classList.remove("btn-success", "btn-danger", "active");
    option3.classList.add("btn-primary");
    option4.classList.remove("btn-success", "btn-danger", "active");
    option4.classList.add("btn-primary");
    option5.classList.remove("btn-success", "btn-danger", "active");
    option5.classList.add("btn-primary");

    title.innerText = "Pergunta " + count;
    question.innerText = data_from_django[count - 1].fields.question;
    option1.innerText = data_from_django[count - 1].fields.answer_1;
    option2.innerText = data_from_django[count - 1].fields.answer_2;
    option3.innerText = data_from_django[count - 1].fields.answer_3;
    option4.innerText = data_from_django[count - 1].fields.answer_4;
    option5.innerText = data_from_django[count - 1].fields.answer_5;

    waitingForNext = false;
}

function nextQuestion() {
    if (data_from_django.length <= count) {
        showResult();
    } else {
        count++;
        
        assignNextQuestion();
    }
}

function showResult() {
    next.remove();
    buttons.remove();

    var titleText = "";
    var questionText = "";

    var rating = countCorrect/count;
    if (rating == 1) {
        titleText = "Parabéns! Você é o bichão mesmo! (" + countCorrect + "/" + count + ")";
        questionText = "Você é um especialista da NBA!";
    } else if (rating >= 0.75) {
        titleText = "Muito bem! Você é quase um bichão! (" + countCorrect + "/" + count + ")";
        questionText = "Você sabe muito sobre a NBA. Continue estudando para se tornar um especialista!";
    } else if (rating >= 0.3) {
        titleText = "Precisa melhorar... você é um piça-fria! (" + countCorrect + "/" + count + ")";
        questionText = "Você possui conhecimentos medianos sobre a NBA!";
    } else if (rating > 0) {
        titleText = "Vish... Deu ruim! (" + countCorrect + "/" + count + ")";
        questionText = "O cachorro do meu pai conhece mais sobre a NBA do que você!";
    } else {
        titleText = "Parabéns aos envolvidos. Você é um animal! (" + countCorrect + "/" + count + ")";
        questionText = "Melhor você acompanhar o campeonato de bocha!";
    }

    title.innerText = titleText;
    question.innerText = questionText;
}

function verifyCorrectAnswer(answer) {
    if (waitingForNext)
        return;

    waitingForNext = true;

    if (answer == data_from_django[count - 1].fields.correct_answer) {
        countCorrect++;
     
        switch (answer) {
            case 1:
                option1.classList.remove("btn-primary");
                option1.classList.add("btn-success");
                break;
            case 2:
                option2.classList.remove("btn-primary");
                option2.classList.add("btn-success");
                break;
            case 3:
                option3.classList.remove("btn-primary");
                option3.classList.add("btn-success");
                break;
            case 4:
                option4.classList.remove("btn-primary");
                option4.classList.add("btn-success");
                break;
            case 5:
                option5.classList.remove("btn-primary");
                option5.classList.add("btn-success");
                break;
        }
    } else {
        switch (answer) {
            case 1:
                option1.classList.remove("btn-primary");
                option1.classList.add("btn-danger");
                break;
            case 2:
                option2.classList.remove("btn-primary");
                option2.classList.add("btn-danger");
                break;
            case 3:
                option3.classList.remove("btn-primary");
                option3.classList.add("btn-danger");
                break;
            case 4:
                option4.classList.remove("btn-primary");
                option4.classList.add("btn-danger");
                break;
            case 5:
                option5.classList.remove("btn-primary");
                option5.classList.add("btn-danger");
                break;
        }
        switch (data_from_django[count - 1].fields.correct_answer) {
            case 1:
                option1.classList.remove("btn-primary");
                option1.classList.add("btn-success");
                break;
            case 2:
                option2.classList.remove("btn-primary");
                option2.classList.add("btn-success");
                break;
            case 3:
                option3.classList.remove("btn-primary");
                option3.classList.add("btn-success");
                break;
            case 4:
                option4.classList.remove("btn-primary");
                option4.classList.add("btn-success");
                break;
            case 5:
                option5.classList.remove("btn-primary");
                option5.classList.add("btn-success");
                break;
        }
    }

    card.appendChild(next);
}

assignNextQuestion();