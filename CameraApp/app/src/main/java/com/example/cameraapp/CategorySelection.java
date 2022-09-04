package com.example.cameraapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.File;
import java.io.IOException;
import java.net.URI;

public class CategorySelection extends AppCompatActivity {

    private static String categorySelected = "Landscape";

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.category_selection);

        Spinner categorySpinner = findViewById(R.id.categorySpinner);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.categoryList, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        categorySpinner.setAdapter(adapter);
        categorySpinner.setSelection(0, true);
        categorySpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                 categorySelected = adapterView.getItemAtPosition(i).toString();
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        Button uploadButton = findViewById(R.id.uploadImage);
        uploadButton.setOnClickListener(v->{
            Toast.makeText(this, categorySelected, Toast.LENGTH_LONG).show();
            String uri = getIntent().getExtras().getString("IMAGE_URI");
            Uri uri1 = Uri.parse(uri);
            System.out.println("*****"+uri1);
        });
    }
}
