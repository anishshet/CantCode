function solve_question(object) {
    localStorage.clear()
    localStorage.setItem("question_id", object.id)
    window.location.href = "ide.html";
}
window.onload = function init() {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    fetch("http://0.0.0.0:5678/question", requestOptions)
        .then(response => response.text())
        .then(result => {
            questions = JSON.parse(result)
            var counter = 0
            for (let i = 0; i <= questions.length; i++) {
                var list_of_questions = document.getElementById("list_of_questions")
                var outer_div = document.createElement("a")
                outer_div.className = "active u-accordion-link u-active-white u-button-style u-custom-font u-hover-white u-text-active-custom-color-1 u-text-hover-custom-color-1 u-white u-accordion-link-1"
                question_id = questions[i]["_id"]
                outer_div.id = question_id

                var outer_span = document.createElement("span");
                outer_span.className = "u-accordion-link-text";
                outer_span.style = "font-size: 1.5625rem";
                var inner_span = document.createElement("span");
                inner_span.onclick = function(){
                    solve_question(this)
                }
                inner_span.style = "font-size: 1.25rem";
                inner_span.id = question_id;
                inner_span.innerHTML = questions[i]["short_desc"];
                outer_span.appendChild(inner_span);
                outer_div.appendChild(outer_span);
                list_of_questions.appendChild(outer_div);
                counter = counter + 1;
            }

        })
        .catch(error => console.log('error', error));

}
