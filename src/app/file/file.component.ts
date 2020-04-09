import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-file',
  templateUrl: './file.component.html',
  styleUrls: ['./file.component.scss']
})
export class FileComponent implements OnInit {
  @ViewChild('FileSelectInputDialog') fileSelectInputDialog: ElementRef;

  constructor() { }

  ngOnInit(): void {
  }

  onSubmit(value: any) {
    console.log(value);
  }

  onLoad() {
    const e: HTMLElement = this.fileSelectInputDialog.nativeElement;
    e.click();
  }

  onFileSelected(event) {
    const file = event.target.files[0]
    console.log(file);
    const data = new FormData();
    data.append("file", file, file.name);
  }
}
