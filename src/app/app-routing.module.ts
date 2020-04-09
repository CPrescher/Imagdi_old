import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FileComponent } from './file/file.component';
import { KaraboDataComponent } from './karabo-data/karabo-data.component';
import { KaraboBridgeComponent } from './karabo-bridge/karabo-bridge.component';


const routes: Routes = [
  {path: 'file', component: FileComponent},
  {path: 'karabo-data', component: KaraboDataComponent},
  {path: 'karabo-bridge', component: KaraboBridgeComponent},
  {path: '', redirectTo: 'file', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
