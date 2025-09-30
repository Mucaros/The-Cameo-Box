let navigationButton = document.querySelector('.navButton')
let navigationElement = document.querySelector('.NavbarElements')
let title = document.querySelector('.Title')

navigationButton.addEventListener('click', () => {
    navigationElement.classList.toggle('active')
    title.classList.toggle('active')

    if (navigationButton.classList.contains('fa-bars')){
        navigationButton.classList.remove('fa-bars')
        navigationButton.classList.add('fa-x')
    } else{
        navigationButton.classList.remove('fa-x')
        navigationButton.classList.add('fa-bars')
    }
})

