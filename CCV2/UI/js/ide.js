let editor;

window.onload = function () {

    editor = ace.edit("editor");
    editor.setTheme("ace/theme/github.js");
    editor.session.setMode("ace/mode/c_cpp");

    editor.setOptions({

        fontSize: '20pt',
        fontFamily: 'Ubuntu Mono',
        enableBasicAutocompletion: true,
        enableLiveAutocompletion: true,
        showPrintMargin: false,
        cursorStyle: 'smooth',
        autoScrollEditorIntoView: true,
        animatedScroll: true,
    });
    fetch("http://0.0.0.0:5678/question/" + localStorage.getItem('question_id'), null)
        .then(response => response.text())
        .then(result => {
            question = JSON.parse(result);
            var description_component = document.getElementById("description");
            description_component.innerHTML = question.long_desc

        })
        .catch(error => console.log('error', error));
    language = localStorage.getItem('language');

    if (language !== null) {
        document.getElementById(language).selected = true;
        const code = localStorage.getItem("code-" + language)
        if (code !== null) {
            editor.setValue(code);
        }
    }
}

function submitcode() {
    const code = editor.getValue()
    let language = $("#language").val();
    let question_id = localStorage.getItem("question_id")
    localStorage.setItem("code-" + language, code);
    localStorage.setItem("language", language);
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = { "code": code, "language": language, "question_id": question_id }
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify(raw),
        redirect: 'follow'
    };

    fetch("http://0.0.0.0:5678/solution", requestOptions)
        .then(response => response.json())
        .then(result => {
            document.getElementById("testcases_result").innerHTML = result;
        })
        .catch(error => console.log('error', error));
}

function changeLanguage() {

    let language = $("#language").val();

    if (language == 'c' || language == 'cpp')
        editor.session.setMode("ace/mode/c_cpp");

    else if (language == 'python')
        editor.session.setMode("ace/mode/python");

    // else if (language == 'java')
    //     editor.session.setMode("ace/mode/java");

}