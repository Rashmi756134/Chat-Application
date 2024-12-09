var typed = new Typed('.text', {
    strings: ["Frontend Developer", "YouTuber", "Web Developer"],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
}
);

const scriptURL = 'https://script.google.com/macros/s/AKfycbz50T8OOvy0uHo4pbJ53IXdvl6w4D3dFkys26FK1l6bmRZsJhDf_2y-cb1VTl2HFzI8/exec'

const form = document.forms['contact-form']



form.addEventListener('submit', e => {

	e.preventDefault()
	fetch(scriptURL, { method: 'POST', body: new FormData(form)})
	.then(response => alert("Thank you! your form is submitted successfully." ))
	.then(() => { window.location.reload(); })
	.catch(error => console.error('Error!', error.message))

 })
