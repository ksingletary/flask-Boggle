// AJAX using axios to retrieve form value


$form_value = $('input').val()

async function ajaxy(){
    const res = await axios({
        url: 'http://127.0.0.1:5000/board',
        method: 'post'
    })
    console.log($form_value)
    return res
}

ajaxy();