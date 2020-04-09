import { NgModule } from '@angular/core';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { MatButtonModule } from '@angular/material/button';


@NgModule({
  imports: [
    MatToolbarModule,
    MatIconModule,
    MatListModule,
    MatButtonModule
  ],
  exports: [
    MatToolbarModule,
    MatIconModule,
    MatListModule,
    MatButtonModule
  ]
})
export class MaterialsModule {

}
