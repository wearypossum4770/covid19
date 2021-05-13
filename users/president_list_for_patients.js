const fs = require('fs')
const ghi = [
  {
    
    first_name: 'George',
    last_name: 'Washington',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: "Pope's Creek",
    birth_state: 'Virginia',
    date_of_birth: '-61307'
  },
   {
    
    first_name: 'John',
    last_name: 'Adams',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Braintree',
    birth_state: 'Massachusetts',
    date_of_birth: '-59961'
  },
{
    
    first_name: 'Thomas',
    last_name: 'Jefferson',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Goochland County',
    birth_state: 'Virginia',
    date_of_birth: '-57239'
  },
  {
    
    first_name: 'James',
    last_name: 'Madison',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Port Conway',
    birth_state: 'Virginia',
    date_of_birth: '-54345'
  },
  {
    
    first_name: 'James',
    last_name: 'Monroe',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Monroe Hall',
    birth_state: 'Virginia',
    date_of_birth: '-51745'
  },
  {
    
    first_name: 'Andrew',
    last_name: 'Jackson',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Waxhaws Region',
    birth_state: 'South/North Carolina',
    date_of_birth: '-48502'
  },
  {
    
    first_name: 'John',
    last_name: 'Adams',
    middle_name: 'Quincy',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Braintree',
    birth_state: 'Massachusetts',
    date_of_birth: '-48384'
  },
  {
    
    first_name: 'William',
    last_name: 'Harrison',
    middle_name: 'Henry',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Charles City County',
    birth_state: 'Virginia',
    date_of_birth: '-46344'
  },
  {
    
    first_name: 'Martin',
    last_name: 'Van Buren',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Kinderhook',
    birth_state: 'New York',
    date_of_birth: '-42758'
  },
  {
    
    first_name: 'Zachary',
    last_name: 'Taylor',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Barboursville',
    birth_state: 'Virginia',
    date_of_birth: '-42038'
  },
   {
    
    first_name: 'John',
    last_name: 'Tyler',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Charles City County',
    birth_state: 'Virginia',
    date_of_birth: '-40087'
  },
  {
    
    first_name: 'James',
    last_name: 'Buchanan',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Cove Gap',
    birth_state: 'Pennsylvania',
    date_of_birth: '-39697'
  },
   {
    
    first_name: 'James',
    last_name: 'Polk',
    middle_name: 'K',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Pineville',
    birth_state: 'North Carolina',
    date_of_birth: '-38043'
  },
  {
    
    first_name: 'Millard',
    last_name: 'Fillmore',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Moravia',
    birth_state: 'New York',
    date_of_birth: '-36516'
  },
  {
    
    first_name: 'Franklin',
    last_name: 'Pierce',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Hillsborough',
    birth_state: 'New Hampshire',
    date_of_birth: '-34735'
  },
  {
    
    first_name: 'Andrew',
    last_name: 'Johnson',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Raleigh',
    birth_state: 'North Carolina',
    date_of_birth: '-33238'
  },
  {
    
    first_name: 'Abraham',
    last_name: 'Lincoln',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Hardin County',
    birth_state: 'Kentucky',
    date_of_birth: '-33193'
  },
  {
    
    first_name: 'Ulysses',
    last_name: 'Grant',
    middle_name: 'S',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Point Pleasant',
    birth_state: 'Ohio',
    date_of_birth: '-28371'
  },
  {
    
    first_name: 'Rutherford',
    last_name: 'Hayes',
    middle_name: 'B',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Delaware',
    birth_state: 'Ohio',
    date_of_birth: '-28211'
  },
   {
    
    first_name: 'Chester',
    last_name: 'Arthur',
    middle_name: 'A',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Fairfield',
    birth_state: 'Vermont',
    date_of_birth: '-25653'
  },
  {
    
    first_name: 'James',
    last_name: 'Garfield',
    middle_name: 'A',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Moreland Hills',
    birth_state: 'Ohio',
    date_of_birth: '-24878'
  },
  {
    
    first_name: 'Benjamin',
    last_name: 'Harrison',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'North Bend',
    birth_state: 'Ohio',
    date_of_birth: '-24238'
  },
  {
    
    first_name: 'Grover',
    last_name: 'Cleveland',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Caldwell',
    birth_state: 'New Jersey',
    date_of_birth: '-22932'
  },
  {
    
    first_name: 'William',
    last_name: 'McKinley',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Niles',
    birth_state: 'Ohio',
    date_of_birth: '-20789'
  },
  {
    
    first_name: 'Woodrow',
    last_name: 'Wilson',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Staunton',
    birth_state: 'Virginia',
    date_of_birth: '-15707'
  },
  {
    
    first_name: 'William',
    last_name: 'Taft',
    middle_name: 'Howard',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Cincinnati',
    birth_state: 'Ohio',
    date_of_birth: '-15446'
  },
  {
    
    first_name: 'Theodore',
    last_name: 'Roosevelt',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'New York City',
    birth_state: 'New York',
    date_of_birth: '-15039'
  },
  {
    
    first_name: 'Warren',
    last_name: 'Harding',
    middle_name: 'G',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Blooming Grove',
    birth_state: 'Ohio',
    date_of_birth: '-12476'
  },
  {
    
    first_name: 'Calvin',
    last_name: 'Coolidge',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Plymouth',
    birth_state: 'Vermont',
    date_of_birth: '-10040'
  },
  {
    
    first_name: 'Herbert',
    last_name: 'Hoover',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'West Branch',
    birth_state: 'Iowa',
    date_of_birth: '-9273'
  },
  {
    
    first_name: 'Franklin',
    last_name: 'Roosevelt',
    middle_name: 'D',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Hyde Park',
    birth_state: 'New York',
    date_of_birth: '-6543'
  },
  {
    
    first_name: 'Harry',
    last_name: 'Truman',
    middle_name: 'S',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Lamar',
    birth_state: 'Missouri',
    date_of_birth: '-5714'
  },
  {
    
    first_name: 'Dwight',
    last_name: 'Eisenhower',
    middle_name: 'D',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Denison',
    birth_state: 'Texas',
    date_of_birth: '-3364'
  },
  {
    
    first_name: 'Lyndon',
    last_name: 'Johnson',
    middle_name: 'B',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Stonewall',
    birth_state: 'Texas',
    date_of_birth: '3162'
  },
  {
    
    first_name: 'Ronald',
    last_name: 'Reagan',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Tampico',
    birth_state: 'Illinois',
    date_of_birth: '4055'
  },
  {
    
    first_name: 'Richard',
    last_name: 'Nixon',
    middle_name: 'M',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Yorba Linda',
    birth_state: 'California',
    date_of_birth: '4758'
  },
   {
    
    first_name: 'Gerald',
    last_name: 'Ford',
    middle_name: 'R',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Omaha',
    birth_state: 'Nebraska',
    date_of_birth: '4944'
  },
  {
    
    first_name: 'John',
    last_name: 'Kennedy',
    middle_name: 'F',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Brookline',
    birth_state: 'Massachusetts',
    date_of_birth: '6359'
  },
   {
    
    first_name: 'George',
    last_name: 'Bush',
    middle_name: 'H.W',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Milton',
    birth_state: 'Massachusetts',
    date_of_birth: '8930'
  },
  {
    
    first_name: 'Jimmy',
    last_name: 'Carter',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Plains',
    birth_state: 'Georgia',
    date_of_birth: '9041'
  },
  {
    
    first_name: 'George',
    last_name: 'Bush',
    middle_name: 'W',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'New Haven',
    birth_state: 'Connecticut',
    date_of_birth: '16989'
  },
  {
    
    first_name: 'Bill',
    last_name: 'Clinton',
    middle_name: 'NMN',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Hope',
    birth_state: 'Arkansas',
    date_of_birth: '17033'
  },
  {
    
    first_name: 'Barack',
    last_name: 'Obama',
    middle_name: 'H',
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Honolulu',
    birth_state: 'Hawaii',
    date_of_birth: '22497'
  },
  {
    
    first_name: 'Donald',
    last_name: 'Trump',
    middle_name: 'John',
    suffix:"Sr",
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Queens, New York City',
    birth_state: 'New York',
    date_of_birth: '1946-06-14T04:00:00.000Z'
  },
{
   first_name: 'Joseph',
    last_name: 'Biden',
    middle_name: 'Robinette',
    suffix:"Jr"
    get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}`},
    get email(){return `${this.first_name}.${this.middle_name}.${this.last_name}@example.com`},
    password:"password123!@#",
    is_superuser:false,
    is_staff:false,
    is_active:true,
    
    birth_city: 'Scranton',
    birth_state: 'PA',
    date_of_birth: 'November 20, 1942'
  	
}  
]

fs.writeFileSync('users.json',JSON.stringify(ghi))
