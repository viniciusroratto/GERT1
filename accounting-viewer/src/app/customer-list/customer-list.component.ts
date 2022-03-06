import { Component, AfterViewChecked, Input } from '@angular/core';

@Component({
  selector: 'app-customer-list',
  templateUrl: './customer-list.component.html',
  styleUrls: ['./customer-list.component.css']
})
export class CustomerListComponent implements AfterViewChecked {

  private _data: any
  public clients: Array<any>
  public pathImages = '../../assets/img_users/'

  @Input()
  get data() { return this._data; }
  set data(value) {
    this._data = value;
  }

  constructor() { }

  ngAfterViewChecked(): void {
    if(this.data) {
      this.clients = this.data['clients']
      console.log(this.clients)
    }
  }

}
